import typing
from click.testing import CliRunner
import _pytest
import pytest
from data import cli
from data import update
from data import processing


@pytest.fixture(params=[('2018-04-24', 0), ('BAD_DATE', 2)])
def date_result(request: _pytest.fixtures.SubRequest) -> typing.Tuple[str, int]:
    return request.param


def noop(*args) -> None: # pylint: disable=unused-argument
    pass


def test_run_all_args(
        date_result: typing.Tuple[str, int],
        monkeypatch: _pytest.monkeypatch.MonkeyPatch,
    ) -> None:
    monkeypatch.setattr(update, 'update', noop)
    monkeypatch.setattr(processing, 'run', noop)
    monkeypatch.setattr(update, 'download_s3', noop)
    monkeypatch.setattr(update, 'upload_s3', noop)

    date, exit_code = date_result

    runner = CliRunner()
    result = runner.invoke(cli.main, args=[
        'run',
        '--date', date,
        '--scan', 'here',
        '--gather', 'here',
        '--upload'
    ])
    assert result.exit_code == exit_code


def test_update(monkeypatch: _pytest.monkeypatch.MonkeyPatch) -> None:
    monkeypatch.setattr(update, 'update', noop)

    runner = CliRunner()
    result = runner.invoke(cli.main, args=[
        'update',
        '--scan', 'here',
        '--gather', 'here',
    ])
    assert result.exit_code == 0


def test_process(
        date_result: typing.Tuple[str, int],
        monkeypatch: _pytest.monkeypatch.MonkeyPatch,
    ) -> None:

    date, exit_code = date_result

    monkeypatch.setattr(processing, 'run', noop)

    runner = CliRunner()
    result = runner.invoke(cli.main, args=[
        'process',
        '--date', date,
    ])
    assert result.exit_code == exit_code


def test_download(monkeypatch: _pytest.monkeypatch.MonkeyPatch) -> None:
    monkeypatch.setattr(update, 'download_s3', noop)

    runner = CliRunner()
    result = runner.invoke(cli.main, args=[
        'download',
    ])
    assert result.exit_code == 0


def test_upload(
        date_result,
        monkeypatch: _pytest.monkeypatch.MonkeyPatch) -> None:

    date, exit_code = date_result
    monkeypatch.setattr(update, 'upload_s3', noop)

    runner = CliRunner()
    result = runner.invoke(cli.main, args=[
        'upload',
        '--date', date
    ])
    assert result.exit_code == exit_code
