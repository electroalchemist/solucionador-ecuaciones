from ecuaciones import resolver_sistema


def test_solucion_unica():
    # x + y = 3, x - y = 1  ->  x = 2, y = 1
    assert resolver_sistema(1, 1, 3, 1, -1, 1) == (2.0, 1.0)


def test_solucion_con_decimales():
    # 2x + y = 1, x + 2y = 1  ->  x = 1/3, y = 1/3
    x, y = resolver_sistema(2, 1, 1, 1, 2, 1)
    assert abs(x - 1 / 3) < 1e-9
    assert abs(y - 1 / 3) < 1e-9


def test_rectas_paralelas():
    # x + y = 1, x + y = 2  ->  sin solución
    assert resolver_sistema(1, 1, 1, 1, 1, 2) is None


def test_rectas_coincidentes():
    # x + y = 1, 2x + 2y = 2  ->  infinitas soluciones
    assert resolver_sistema(1, 1, 1, 2, 2, 2) is None