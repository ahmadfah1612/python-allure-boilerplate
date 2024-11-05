class PostBuilder:
    def __init__(self):
        self.reset()

    def reset(self):
        self._post = {
            "title": None,
            "body": None,
            "userId": None
        }
        return self

    def with_title(self, title):
        self._post["title"] = title
        return self

    def with_body(self, body):
        self._post["body"] = body
        return self

    def with_user_id(self, user_id):
        self._post["userId"] = user_id
        return self

    def build(self):
        post = {k: v for k, v in self._post.items() if v is not None}
        self.reset()
        return post
