from django.urls import re_path

from course.urls import EDIT_URL_PREFIX
from . import views


MODEL_URL_PREFIX = EDIT_URL_PREFIX + r'(?P<model>[\w\d\-]+)/'

urlpatterns = [
    re_path(EDIT_URL_PREFIX + r'$',
        views.EditContentView.as_view(),
        name='course-edit'),
    re_path(EDIT_URL_PREFIX + r'gitmanager/$',
        views.EditGitmanagerView.as_view(),
        name='gitmanager-details'),
    re_path(EDIT_URL_PREFIX + r'instances/$',
        views.CloneInstanceView.as_view(),
        name='course-clone'),
    re_path(EDIT_URL_PREFIX + r'course/$',
        views.EditInstanceView.as_view(),
        name='course-details'),
    re_path(EDIT_URL_PREFIX + r'index/$',
        views.EditIndexView.as_view(),
        name='course-index'),
    re_path(EDIT_URL_PREFIX + r'configure-content/$',
        views.ConfigureContentView.as_view(),
        name='course-configure'),
    re_path(EDIT_URL_PREFIX + r'course-build-log/$',
        views.BuildLogView.as_view(),
        name='course-build-log'),
    re_path(EDIT_URL_PREFIX + r'tags/$',
        views.UserTagListView.as_view(),
        name='course-tags'),
    re_path(EDIT_URL_PREFIX + r'tags/new/$',
        views.UserTagAddView.as_view(),
        name='course-tags-add'),
    re_path(EDIT_URL_PREFIX + r'tags/(?P<tag_id>\d+)/edit$',
        views.UserTagEditView.as_view(),
        name='course-tags-edit'),
    re_path(EDIT_URL_PREFIX + r'tags/(?P<tag_id>\d+)/remove$',
        views.UserTagDeleteView.as_view(),
        name='course-tags-remove'),
    re_path(EDIT_URL_PREFIX + r'tags/(?P<tag_id>\d+)/new-tagging$',
        views.UserTaggingAddView.as_view(),
        name='course-taggings-add'),
    re_path(EDIT_URL_PREFIX + r'submission-tags/$',
            views.SubmissionTagListView.as_view(),
            name='course-submission-tags'),
    re_path(EDIT_URL_PREFIX + r'submission-tags/new/$',
            views.SubmissionTagAddView.as_view(),
            name='course-submission-tags-add'),
    re_path(EDIT_URL_PREFIX + r'submission-tags/(?P<tag_id>\d+)/edit$',
            views.SubmissionTagEditView.as_view(),
            name='course-submission-tags-edit'),
    re_path(EDIT_URL_PREFIX + r'submission-tags/(?P<tag_id>\d+)/remove$',
            views.SubmissionTagDeleteView.as_view(),
            name='course-submission-tags-remove'),
    re_path(EDIT_URL_PREFIX + r'batch-assess/$',
        views.BatchCreateSubmissionsView.as_view(),
        name='batch-assess'),

    re_path(MODEL_URL_PREFIX + r'add/$',
        views.ModelEditView.as_view(),
        name='model-create'),
    re_path(MODEL_URL_PREFIX + r'add/(?P<parent_id>\d+)/$',
        views.ModelEditView.as_view(),
        name='model-create-for'),
    re_path(MODEL_URL_PREFIX + r'add/(?P<parent_id>\d+)/(?P<type>[\w\d\-]+)/$',
        views.ModelEditView.as_view(),
        name='model-create-type-for'),
    re_path(MODEL_URL_PREFIX + r'(?P<id>\d+)/$',
        views.ModelEditView.as_view(),
        name='model-edit'),
    re_path(MODEL_URL_PREFIX + r'(?P<id>\d+)/delete/$',
        views.ModelDeleteView.as_view(),
        name='model-remove'),
]
