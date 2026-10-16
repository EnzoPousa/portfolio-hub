gerar([A, B, C, D]) :-
    select(A, [1,2,3,4,5,6,7,8,9], R1),
    select(B, R1, R2),
    select(C, R2, R3),
    select(D, R3, _).

%funcao que cria as regras das variaves

testar([A, B, C, D]) :-
    A < B,
    A < C,
    D is B - A,
    D mod 2 =:= 0,
    C is B + 4,
    B =:= 5.

cofre(S) :-
    gerar(S),
    testar(S).