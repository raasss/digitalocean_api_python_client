class Region(object):
    def __init__(self,
                 slug,
                 name,
                 sizes,
                 available,
                 features):
        self.slug = slug
        self.name = name
        self.sizes = sizes
        self.available = available
        self.features = features
