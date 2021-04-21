import logging

from scrapy import Request, Spider
from scrapy.core.downloader.handlers.http import HTTPDownloadHandler


class RotatingProxiesDownloadHandler(HTTPDownloadHandler):
    logger = logging.getLogger(name=__name__)

    def download_request(self, request: Request, spider: Spider):
        """Return a deferred for the HTTP download"""
        if spider.settings.get(
            "ROTATING_PROXIES_DOWNLOADER_HANDLER_AUTO_CLOSE_CACHED_CONNECTIONS_ENABLED"
        ) or request.meta.get("close_cached_connections"):
            self.logger.debug(f"close cached connections for {request.url}")
            self._pool.closeCachedConnections()

        return super().download_request(request, spider)
