from tortoise import fields, Model


class SavedTextSimplification(Model):
    id = fields.IntField(primary_key=True)
    created_at = fields.DatetimeField(auto_now_add=True)

    text = fields.TextField(null=False)
    proofreading = fields.TextField(null=False)
    lex = fields.TextField(null=False)
    connectives = fields.TextField(null=False)
    expressions = fields.TextField(null=False)
    sentence_splitter = fields.TextField(null=False)
    nominalizations = fields.TextField(null=False)
    verbs = fields.TextField(null=False)
    sentence_reorganizer = fields.TextField(null=False)
    explain = fields.TextField(null=True)

    q1 = fields.TextField(null=True)
    q2 = fields.TextField(null=True)
    q3 = fields.TextField(null=True)

    class Meta:
        table = "text_simplification"