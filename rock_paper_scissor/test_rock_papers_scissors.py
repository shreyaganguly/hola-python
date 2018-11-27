import rock_papers_scissors
import mock
import builtins

def test_prettify():
    assert rock_papers_scissors.prettify("r") == "Rock(O)"
    assert rock_papers_scissors.prettify("p") == "Paper(__)"
    assert rock_papers_scissors.prettify("s") == "Scissor(8<)"


def test_evaluate_output():
    assert rock_papers_scissors.evaluate_output("r", "r") == 0
    assert rock_papers_scissors.evaluate_output("r", "p") == 1
    assert rock_papers_scissors.evaluate_output("r", "s") == -1
    assert rock_papers_scissors.evaluate_output("p", "r") == -1
    assert rock_papers_scissors.evaluate_output("p", "p") == 0
    assert rock_papers_scissors.evaluate_output("p", "s") == 1
    assert rock_papers_scissors.evaluate_output("s", "r") == 1
    assert rock_papers_scissors.evaluate_output("s", "p") == -1
    assert rock_papers_scissors.evaluate_output("s", "s") == 0


def test_get_game_status():
    assert rock_papers_scissors.get_game_status(0) == "DRAW!!!!"
    assert rock_papers_scissors.get_game_status(1) == "YOU WON!!!!"
    assert rock_papers_scissors.get_game_status(-1) == "YOU LOST!!!!"


def test_init_game(capsys):
    with mock.patch.object(builtins, 'input', lambda _: 'dfg'):
        rock_papers_scissors.init_rock_paper_scissor_game()
        captured = capsys.readouterr()
        assert "Wrong input! Please correct and try again\n" in captured.out


def test_game_success(capsys):
    with mock.patch.object(builtins, 'input', lambda _: 'r'):
        rock_papers_scissors.play_game(1)
        captured = capsys.readouterr()
        assert "THE LEAGUE" in captured.out


def test_game_error(capsys):
    with mock.patch.object(builtins, 'input', lambda _: 'g'):
        rock_papers_scissors.play_game(1)
        captured = capsys.readouterr()
        assert "Wrong input! Please correct and try again" in captured.out


def test_print_outcome(capsys):
    rock_papers_scissors.print_outcome(0)
    captured = capsys.readouterr()
    assert "THE LEAGUE IS A DRAW!!!" in captured.out
    rock_papers_scissors.print_outcome(-1)
    captured = capsys.readouterr()
    assert "YOU LOST THE LEAGUE!!!! Hard luck!!" in captured.out
    rock_papers_scissors.print_outcome(1)
    captured = capsys.readouterr()
    assert "YOU WON THE LEAGUE!!!! Yaay!!" in captured.out

def test_evaluate_per_outcome_result():
    assert rock_papers_scissors.evaluate_per_outcome_result(0, 1, 2)[0] == 1
    assert rock_papers_scissors.evaluate_per_outcome_result(0, 1, 2)[1] == 2
    assert rock_papers_scissors.evaluate_per_outcome_result(-1, 1, 2)[0] == 1
    assert rock_papers_scissors.evaluate_per_outcome_result(-1, 1, 2)[1] == 3
    assert rock_papers_scissors.evaluate_per_outcome_result(1, 1, 2)[0] == 2
    assert rock_papers_scissors.evaluate_per_outcome_result(1, 1, 2)[1] == 2

def test_evaluate_league_outcome(capsys):
    rock_papers_scissors.evaluate_league_outcome(1,0,1,2)
    captured = capsys.readouterr()
    assert "YOU LOST THE LEAGUE!!!! Hard luck!!" in captured.out
    rock_papers_scissors.evaluate_league_outcome(1,0,2,1)
    captured = capsys.readouterr()
    assert "YOU WON THE LEAGUE!!!! Yaay!!" in captured.out
    rock_papers_scissors.evaluate_league_outcome(1,0,1,1)
    captured = capsys.readouterr()
    assert "THE LEAGUE IS A DRAW!!!" in captured.out
    rock_papers_scissors.evaluate_league_outcome(0,2,1,2)
    captured = capsys.readouterr()
    assert "YOU LOST THE LEAGUE!!!! Hard luck!!" in captured.out
    rock_papers_scissors.evaluate_league_outcome(0,2,2,1)
    captured = capsys.readouterr()
    assert "YOU WON THE LEAGUE!!!! Yaay!!" in captured.out
