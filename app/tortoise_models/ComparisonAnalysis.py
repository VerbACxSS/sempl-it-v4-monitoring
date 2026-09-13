from tortoise import fields, Model


class SavedComparisonAnalysis(Model):
    id = fields.IntField(primary_key=True)
    created_at = fields.DatetimeField(auto_now_add=True)

    text1 = fields.TextField(null=False)
    text2 = fields.TextField(null=False)

    class Meta:
        table = "comparison_analysis"