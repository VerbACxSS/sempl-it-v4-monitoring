from app.models.SimplificationRequest import SimplificationRequest
from app.tortoise_models import SavedTextAnalysis, SavedComparisonAnalysis
from app.tortoise_models.TextSimplification import SavedTextSimplification


class SavingService:
    @staticmethod
    async def save_text_analysis(text: str) -> int:
        analysis = await SavedTextAnalysis.create(text=text)
        return analysis.id

    @staticmethod
    async def save_comparison_analysis(text1: str, text2: str) -> int:
        analysis = await SavedComparisonAnalysis.create(text1=text1, text2=text2)
        return analysis.id

    @staticmethod
    async def save_simplification(simplification_progress: SimplificationRequest) -> int:
        simplification = await SavedTextSimplification.create(mode=simplification_progress['mode'],
                                                              text=simplification_progress['original'],
                                                              proofreading=simplification_progress['proofreading'],
                                                              lex=simplification_progress['lex'],
                                                              connectives=simplification_progress['connectives'],
                                                              expressions=simplification_progress['expressions'],
                                                              sentence_splitter=simplification_progress['sentence_splitter'],
                                                              nominalizations=simplification_progress['nominalizations'],
                                                              verbs=simplification_progress['verbs'],
                                                              sentence_reorganizer=simplification_progress['sentence_reorganizer'],
                                                              explain=simplification_progress['explain'],)
        return simplification.id

    @staticmethod
    async def update_simplification(simplification_id: int, q1: str, q2: str, q3: str) -> None:
        simplification = await SavedTextSimplification.get(id=simplification_id)
        simplification.q1 = q1
        simplification.q2 = q2
        simplification.q3 = q3
        await simplification.save()