// Copyright 2000-2019 JetBrains s.r.o. Use of this source code is governed by the Apache 2.0 license that can be found in the LICENSE file.
package org.jetbrains.plugins.github.pullrequest.comment.ui

import com.intellij.ui.CollectionListModel
import org.jetbrains.plugins.github.api.data.pullrequest.GHPullRequestReviewThread

class GHPRReviewThreadModelImpl(thread: GHPullRequestReviewThread)
  : CollectionListModel<GHPRReviewCommentModel>(thread.comments.map(GHPRReviewCommentModel.Companion::convert)),
    GHPRReviewThreadModel {

  override val id: String = thread.id
  override val createdAt = thread.createdAt
  override val filePath = thread.path
  override val diffHunk = thread.diffHunk
  override val firstCommentDatabaseId = thread.firstCommentDatabaseId

  override fun update(thread: GHPullRequestReviewThread) {
    var removed = 0
    for (i in 0 until items.size) {
      val idx = i - removed
      val newComment = thread.comments.getOrNull(idx)
      if (newComment == null) {
        removeRange(idx, items.size - 1)
        break
      }

      val comment = items.getOrNull(idx) ?: break
      if (comment.id == newComment.id) {
        if (comment.update(newComment))
          fireContentsChanged(this, idx, idx)
      }
      else {
        remove(idx)
        removed++
      }
    }

    if (size == thread.comments.size) return
    val newComments = thread.comments.subList(size, thread.comments.size)
    add(newComments.map { GHPRReviewCommentModel.convert(it) })
  }

  override fun addComment(comment: GHPRReviewCommentModel) {
    add(comment)
  }

  override fun equals(other: Any?): Boolean {
    if (this === other) return true
    if (other !is GHPRReviewThreadModelImpl) return false

    if (id != other.id) return false

    return true
  }

  override fun hashCode(): Int {
    return id.hashCode()
  }
}