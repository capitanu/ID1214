
:- dynamic on/2.

on(a,b).    
on(b,c).    
on(c,spot1).

:- dynamic prev/2.

prev(a,spot1).
prev(b,spot1).
prev(c,spot1).

:- dynamic top/2.
top(a,spot1).
top(spot2,spot2).
top(spot3,spot3).

:- dynamic spot/2.
spot(a,spot1).
spot(b,spot1).
spot(c,spot1).
spot(spot1,spot1).
spot(spot2,spot2).
spot(spot3,spot3).


preserve_alph_ord(A,B) :-
    (((A == a) ; (A == b, B == c) ; (B == spot1) ; (B == spot2) ; (B == spot3)) -> true; false).

is_adjacent(A,B) :-
    spot(A,X),
    spot(B,Y),
    ((X == Y ; X == spot2; Y == spot2) -> true ; false).

clear_all(A,B) :-
    clear_off(A),
    clear_off(B),
    (on(X,A) -> clear_all(A,B); true),
    (on(X,B) -> clear_all(A,B); true).
    

put_on(A,B) :-
    on(A,B).
put_on(A,B) :-
    not(on(A,B)),
    \+(A == spot1),
    \+(A == spot2),
    \+(A == spot3),
    (not(preserve_alph_ord(A,B)) -> on(B,Z), clear_off(Z), put_on(A,Z); true,
    (not(is_adjacent(A,B)) -> top(H,spot2), put_on(A,H); true), 
    \+(A == B),
    clear_all(A,B),
    on(A,X),
    retract(spot(A,_)),
    spot(X,S),
    assert(spot(A,S)),
    retract(on(A,X)),
    assert(on(A,B)),
    spot(X,O),
    retract(prev(A,_)),
    assert(prev(A,O)),
    top(A,T),
    top(B,R),
    retract(spot(A,_)),
    assert(spot(A,R)),
    retract(top(A,_)),
    assert(top(X,T)),
    retract(top(B,_)),
    assert(top(A,R)),
    assert(move(A,X,B))).

clear_off(table).    
clear_off(A) :-      
    not(on(_X,A)).
clear_off(A) :-
    on(X,A),
    clear_off(X),
    spot(X,S),
    ((S == spot1; S == spot3) -> top(Z,spot2) ;
     (prev(X,spot1) -> top(Z,spot3) ; top(Z,spot1))),
    put_on(X,Z).

do(Glist) :- 
    do_all(Glist,Glist).

do_all([G|R],Allgoals) :-  
    call(G),
    do_all(R,Allgoals),!.  

do_all([G|_],Allgoals) :-  
    achieve(G),
    do_all(Allgoals,Allgoals).
do_all([],_Allgoals).         

achieve(on(A,B)) :-
    put_on(A,B).
