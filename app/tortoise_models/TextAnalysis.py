from tortoise import fields, Model


class SavedTextAnalysis(Model):
    id = fields.IntField(primary_key=True)
    created_at = fields.DatetimeField(auto_now_add=True)

    text = fields.TextField(null=False)

    class Meta:
        table = "text_analysis"