from django.contrib.auth.models import User
from django.db import models
#from reviewboard.reviews.models import Review, ReviewRequest
from reviewboard.reviews.models import FileDiff
from datetime import datetime
from django.utils.translation import ugettext_lazy as _

class ChangeInfoForFileDiff(models.Model):
    '''
    review_request = models.ForeignKey(ReviewRequest,
        related_name="reviewing_sessions", blank=False)
    user = models.ForeignKey(User,
        related_name="review_request_reviewing_sessions", blank=False)
    review = models.OneToOneField(Review, related_name="reviewing_session",
        blank=True, null=True)
    last_updated = models.DateTimeField(default=datetime.now, auto_now=True,
        blank=False)
    working_seconds = models.PositiveIntegerField(default=0, blank=False)
    '''
    file_diff = models.ForeignKey(FileDiff,
        related_name="reviewing_lines_for_file_diff", blank=False)
    mod_line = models.PositiveIntegerField(_("mod_line"))
    del_line = models.PositiveIntegerField(_("del_line"))
    
    class Meta:
        #unique_together = ("review_request", "user", "review")
        #unique_together = ("file_diff")
        pass
