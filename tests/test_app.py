from typer.testing import CliRunner

from app.app import app

runner = CliRunner()


def test_default_length():
    result = runner.invoke(app)
    assert result.exit_code == 0
    assert len(result.stdout) == 17


def test_short_password_fail():
    result = runner.invoke(app, ["--length", "5"], input="n")
    assert result.exit_code == 1


def test_short_password_pass():
    result = runner.invoke(app, ["--length", "5"], input="y")
    assert result.exit_code == 0
