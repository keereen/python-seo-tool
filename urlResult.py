from collections import namedtuple


class UrlResult:
    """Tracks status code and attributes for a scanned url

    Helps distinguish different types of links.

    eg:

    - iframe
    - image
    - script

    This class also tracks other important attributes like parent url or
    if its a redirect url which can be used in the HTML report

    Typical usage example:

    result = UrlResult(link, 0)
    result.setUrlAsImage()

    Attributes:
        url: The url that has been scanned
        statusCode: The status code of the url that has been scanned
    """

    def __init__(self, url, statusCode):

        # initialise with a url string
        # and statusCode integer
        self.url = url
        self.statusCode = statusCode

        # parentUrls is an array of
        # ParentUrlText named tuples
        self.parentUrls = []

        # default to no redirect, and internal Link
        self.redirectLocation = None
        self.isOfType = "link"
        self.isUrlInternal = True

    def getURL(self):
        return self.url

    def getStatusCode(self):
        return self.statusCode

    def setStatusCode(self, aStatusCode):
        self.statusCode = aStatusCode

    def getParentUrl(self):
        """
        Parent URLs are stored in an array.
        If no parent then return None otherwise
        return the first ParentUrlText tuple in the array
        """
        if len(self.parentUrls) == 0:
            return None
        return self.parentUrls[0]

    def getParentUrls(self):
        return self.parentUrls

    def setRedirectLocation(self, location):
        self.redirectLocation = location

    def getRedirectLocation(self):
        return self.redirectLocation

    def addParentUrl(self, url, text):
        """
        When given a String url and the text of the link on the page
        create a namedtuple of ParentUrlText to store the values
        and add to the array of parentUrls
        """
        if text is None:
            text = ""
        ParentUrlText = namedtuple("ParentUrlText", ["text", "url"])
        parentUrlText = ParentUrlText(text, url)
        self.parentUrls.append(parentUrlText)

    def setUrlAsImage(self):
        self.isOfType = "image"

    def setUrlAsHeadLink(self):
        self.isOfType = "headlink"

    def setUrlAsScript(self):
        self.isOfType = "script"

    def setUrlAsIFrame(self):
        self.isOfType = "iframe"

    def setIsInternal(self, internal):
        self.isUrlInternal = internal

    def isInternal(self):
        return self.isUrlInternal

    def isA(self):
        return self.isOfType

    def isImage(self):
        return self.isOfType == "image"

    def isLink(self):
        return self.isOfType == "link"

    def isHeadLink(self):
        return self.isOfType == "headlink"

    def isScript(self):
        return self.isOfType == "script"

    def isIFrame(self):
        return self.isOfType == "iframe"
