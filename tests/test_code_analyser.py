from code_analyser import analyze_file


def test_analyze_code_py_returns_dict():
    res = analyze_file("code.py")
    assert isinstance(res, dict)
    assert "health_score" in res
    assert "line_metrics" in res
    assert res["line_metrics"]["total_lines"] > 0
    assert isinstance(res.get("warnings"), list)
