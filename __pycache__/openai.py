import os
import openai
openai.organization = "org-YMBX1MiF1GySMhzPY3Lwpq63"
openai.api_key = os.getenv("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")
openai.Model.list()