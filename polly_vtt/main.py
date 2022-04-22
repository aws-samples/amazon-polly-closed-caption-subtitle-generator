import click

from .polly_vtt import PollyVTT


@click.command(
    context_settings=dict(
        ignore_unknown_options=True,
        allow_extra_args=True,
    )
)
@click.argument("base_filename")
@click.argument("voice_id")
@click.argument("output_format")
@click.argument("text")
@click.option("--caption-format", default="vtt", help="'srt' or 'vtt'")
@click.pass_context
def main(ctx, base_filename, voice_id, output_format, text, caption_format):
    polly_options = {ctx.args[i][2:]: ctx.args[i + 1] for i in range(0, len(ctx.args), 2)}
    base_options = {"VoiceId": voice_id, "OutputFormat": output_format, "Text": text}
    options = {**base_options, **polly_options}

    polly_vtt = PollyVTT()
    polly_vtt.generate(base_filename, caption_format, **options)


if __name__ == "__main__":
    main()
