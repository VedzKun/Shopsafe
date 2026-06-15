class BaseDetector:
    def detect(self, page_data):
        raise NotImplementedError(
            "Detector must implement detect() method"
        )
    #this will be inherited y different classes later on