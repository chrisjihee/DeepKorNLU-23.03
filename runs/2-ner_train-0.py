from nlpbook.arguments import *
from nlpbook.ner import cli

args = TrainerArguments(
    env=ProjectEnv(
        project="DeepKorNLU",
        running_gpus="0",
    ),
    data=DataOption(
        home="data",
        name="klue-ner-mini",
        files=DataFiles(
            train="klue-ner-v1.1_train.jsonl",
            valid="klue-ner-v1.1_dev.jsonl"
        ),
        redownload=False,
    ),
    model=ModelOption(
        # pretrained="model/pretrained-pro/ETRI-RoBERTa-Base-bbpe23.03",
        # pretrained="model/pretrained-pro/ETRI-RoBERTa-Base-bbpe22.07",
        # pretrained="model/pretrained-com/KLUE-RoBERTa",
        pretrained="model/pretrained-com/KPF-BERT",
        finetuning_home="model/finetuning",
        finetuning_name="{epoch:02d}, {step:04d}, {val_loss:.3f}, {val_acc:.3f}, {val_chr_f1:.3f}, {val_ent_f1:.3f}",
        max_seq_length=64,
    ),
    hardware=HardwareOption(
        accelerator="gpu",
        batch_size=80,
        precision=16,
    ),
    learning=LearningOption(
        condition="max val_chr_f1",
        val_check=0.5,
        num_save=3,
        epochs=3,
        speed=5e-5,
        seed=7,
    ),
)
with ArgumentsUsing(args) as args_file:
    cli.train(args_file)