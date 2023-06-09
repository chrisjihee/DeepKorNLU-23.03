from nlpbook.arguments import *
from nlpbook.cls import cli

args = ServerArguments(
    env=ProjectEnv(project="DeepKNLU"),
    data=DataOption(name="nsmc"),
    model=ModelOption(
        pretrained="pretrained-com/KcBERT-Base",
        finetuning_home="finetuning",
        max_seq_length=50,
    ),
)
with ArgumentsUsing(args) as args_file:
    cli.serve(args_file)
