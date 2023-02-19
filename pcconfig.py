import pynecone as pc

config = pc.Config(
    app_name="deeptools_ai_website",
    db_url="sqlite:///pynecone.db",
    env=pc.Env.DEV,
)
