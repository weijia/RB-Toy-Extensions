# Reports extension for Review Board.
from django.conf import settings
from django.conf.urls.defaults import patterns, include
from reviewboard.extensions.base import Extension
from reviewboard.extensions.hooks import DashboardHook, URLHook
from reviewboard.extensions.hooks import ChunkGenerationCompleteHook
from models import ChangeInfoForFileDiff

class RBReviewLinesDashboardHook(DashboardHook):
    def get_entries(self):
        return [{
            'label': 'Review lines statistics',
            'url': settings.SITE_ROOT + 'rbreviewlines/',
        }]

class RBReviewLinesChunkGenerationCompleteHook(ChunkGenerationCompleteHook):
    def processChunks(self, file_diff, chunks):
        print '-----------------------------------', file_diff
        print ChangeInfoForFileDiff.objects.get_or_create(file_diff = file_diff,
                    mod_line = 0, del_line = 0)
        for i in chunks:
            #print '-----------------------------------', i
            pass
        
class RBReviewLinesExtension(Extension):
    is_configurable = True
    #requirements = ['extc.extension.ExtCExtension']

    def __init__(self):
        Extension.__init__(self)
        self.dashboard_hook = RBReviewLinesDashboardHook(self)
        # The following line must be added for extension to show an entry
        # in the left side of dashboard
        self.dashboard_hook.entries = self.dashboard_hook.get_entries()
        self.chunkProcessHook = RBReviewLinesChunkGenerationCompleteHook(self)
        print self.chunkProcessHook.hooks
        