from urllib.parse import urljoin

from django.conf import settings
from django_oss_storage.backends import OssStorage
class OssStaticStorage(OssStorage):
    def __init__(self):
        self.location = settings.STATIC_URL
        self.bucket_url = settings.OSS_BUCKET_URL
        super(OssStaticStorage, self).__init__()

    def url(self, name, expire=None):
        key = self._get_key_name(name)
        return urljoin(self.bucket_url,key)

    def save(self, name, content, max_length=None):
        return super(OssStaticStorage, self)._save(name, content)


class OssMediaPublicStorage(OssStorage):
    def __init__(self):
        self.location = settings.MEDIA_URL
        self.bucket_url = settings.OSS_BUCKET_URL
        super(OssMediaPublicStorage, self).__init__()

    def url(self, name, expire=None):
        key = self._get_key_name(name)
        return urljoin(self.bucket_url, key)


class OssMediaPrivateStorage(OssStorage):
    def __init__(self):
        self.location = settings.MEDIA_URL
        self.bucket_url = settings.OSS_BUCKET_URL
        super(OssMediaPrivateStorage, self).__init__()

    def url(self, name, expire=5 * 60):
        key = self._get_key_name(name)
        return self.bucket.sign_url('GET', key, expire)