from pecan import expose, redirect
import wsmeext.pecan as wsme_pecan
import pecan
from pecan import rest

import wsme.types as wtypes

from wsme.types import File


import zipfile
import tarfile

import glob
import os
import json
import uuid
import datetime
import shutil

from io import BytesIO
from joulupukki.controllers.v2.datamodel.build import Build, APIBuild
from joulupukki.controllers.v2.datamodel.user import User
from joulupukki.controllers.v2.datamodel.project import Project
from joulupukki.controllers.v2.datamodel.job import Job


from joulupukki.lib.queues import build_tasks
from joulupukki.lib.distros import supported_distros, reverse_supported_distros


archive_types = {"zip": "application/zip",
                 "tgz": "application/x-gzip",
                }


class JobController(rest.RestController):
    def __init__(self, job_id=None):
        pecan.request.context['job_id'] = job_id
        self.id_ = job_id

    @wsme_pecan.wsexpose(Job)
    def get(self):
        """Returns log of a specific distro."""
        project_name = pecan.request.context['project_name']
        user = User.fetch(pecan.request.context['username'])
        project = Project.fetch(user, project_name)
        build_id = pecan.request.context['build_id']
        if build_id in ["latest"]:
            build_id = project.get_latest_build()
        build = Build.fetch(project, build_id, full_data=True)
        job = Job.fetch(build, self.id_, False)
        return job
 
    @pecan.expose()
    def _lookup(self, *remainder):
        return JobSubController(), remainder


class JobsController(rest.RestController):

    @wsme_pecan.wsexpose([Job])
    def get(self):
        """Returns log of a specific distro."""
        project_name = pecan.request.context['project_name']
        user = User.fetch(pecan.request.context['username'])
        project = Project.fetch(user, project_name)
        build_id = pecan.request.context['build_id']
        if build_id in ["latest"]:
            build_id = project.get_latest_build()
        build = Build.fetch(project, build_id, full_data=True)
           
        jobs = [Job.fetch(build, j_id, False) for j_id in build.get_jobs()]
        jobs = [j for j in jobs if j]
        return jobs


    @pecan.expose()
    def _lookup(self, job_id, *remainder):
        return JobController(job_id), remainder


class LogController(rest.RestController):

    # curl -X GET http://127.0.0.1:8080/v2/titilambert/kaji/builds/8/jobs/1/log
    @expose(content_type='text/plain')
    def get(self):
        """Returns log of a specific job."""
        project_name = pecan.request.context['project_name']
        user = User.fetch(pecan.request.context['username'])
        project = Project.fetch(user, project_name)
        build_id = pecan.request.context['build_id']
        if build_id in ["latest"]:
            build_id = project.get_latest_build()
        build = Build.fetch(project, build_id, full_data=True)
        job_id = pecan.request.context['job_id'] 
        job = Job.fetch(build, job_id, full_data=True)
        return job.get_log()





class JobSubController(rest.RestController):
    log = LogController()



