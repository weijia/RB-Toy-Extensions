from django.contrib.auth.models import User
from django.db import models
from reviewboard.reviews.models import Review, ReviewRequest
from datetime import datetime

class ReviewingLinesForFile(models.Model):
    review_request = models.ForeignKey(ReviewRequest,
        related_name="reviewing_lines_for_file", blank=False)
    '''
    user = models.ForeignKey(User,
        related_name="review_request_reviewing_lines_for_file", blank=False)
    '''
    review = models.OneToOneField(Review, related_name="reviewing_lines_for_file",
        blank=True, null=True)
    working_seconds = models.PositiveIntegerField(default=0, blank=False)

    class Meta:
        #unique_together = ("review_request", "user", "review")
        unique_together = ("review_request", "review")
