class Input:

    def __init__(self,
                 key,
                 label,
                 inputType='string',
                 value=None,
                 required=False,
                 options=None,
                 info=None):
        self.key = key
        self.label = label
        self.type = inputType
        self.value = value
        self.required = required
        self.options = options
        self.info = info
