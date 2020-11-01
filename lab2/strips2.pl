/* prolog tutorial 2.19  Actions and plans */

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

on_first(spot1) :-
    true.
on_first(A) :-
    on(A,X),
    on_first(X).

on_middle(A) :-
    on(A, spot2).
on_middle(A) :-
    on(A,X),
    on_middle(X).

on_last(spot3) :-
    true.
on_last(A) :-
    on(A,X),
    on_last(X).

preserve_alph_ord(b,a) :-
    false.
preserve_alph_ord(c,b) :-
    false.
preserve_alph_ord(c,a) :-
    false.
preserve_alph_ord(_,_) :-
    true.

is_adjecent(A,B) :-
    not((on_first(A),on_last(B)) ; (on_first(B) , on_last(A))).


spot_is1(A) :-
    on(A,X) -> spot_is1(X);
    X == spot1 -> true; false.
    
spot_is2(A) :-
    on(A,X) -> spot_is2(X);
    X == spot2 -> true; false.
    
top_spot1(A) :-
    on(X,A) -> top_spot1(X);
    X == spot1 -> true; false.

top_spot2(A) :-
    on(X,A) -> top_spot2(X);
    X == spot2 -> true; false.

top_spot3(A) :-
    on(X,A) -> top_spot3(X);
    X == spot3 -> true; false.

next_is_2(A,X) :-
    (X == spot1; X == spot3).

next_is_1(A,X) :-
    ((X == spot3), top_spot2(A)).

next_is_3(A,X) :-
    ((X == spot1), top_spot2(A)).


put_on(A,B) :-
    on(A,B).
put_on(A,B) :-
    not(on(A,B)),
    preserve_alph_ord(A,B),
    (not(is_adjecent(A,B)) -> put_on(A,spot2); true),
    \+(A == spot1),
    \+(A == spot2),
    \+(A == spot3),    
    \+(A == B),
    clear_off(A),      
    clear_off(B),
    on(A,X),
    \+(X == B),
    (spot_is1(X) -> retract(prev(A, _)), assert(prev(A,spot1)) ;
     (spot_is2(X) -> retract(prev(A, _)), assert(prev(A,spot2)) ;
     retract(prev(A,_)),assert(prev(A,spot3)))),
    retract(on(A,X)),
    assert(on(A,B)),
    (spot_is1(A) -> retract(top(_,spot1), assert(top(A, B))) ;
     (spot_is2(A) -> retract(top(_,spot2)), assert(top(A,B))) ;
     retract(top(_,spot3)), assert(top(A,B))),
    assert(move(A,X,B)).

clear_off(spot1).
clear_off(spot2).
clear_off(spot3).
clear_off(A) :-     
    not(on(_X,A)).
clear_off(A) :-
    \+(A == spot1),
    \+(A == spot2),
    \+(A == spot3),
    on(X,A),
    clear_off(X),
    prev(X,Y),
    (spot_is1(A) -> retract(prev(X, _)), assert(prev(X,spot1)) ;
     (spot_is2(A) -> retract(prev(X, _)), assert(prev(X,spot2)) ;
     retract(prev(X,_)), assert(prev(X,spot3)))),
    retract(on(X,A)),
    (next_is_1(X,Y) ->
	 top(T, spot1), (not(preserve_alph_ord(X,T)) -> on(T,U), clear_off(U);
	 \+(A == spot1), assert(on(X,spot1)), retract(top(_,spot1)), assert(top(X,spot1)), assert(move(X,A,spot1))) ;
     (next_is_2(X,Y)) ->
	 top(T, spot2), (not(preserve_alph_ord(X,T)) -> on(T,U), clear_off(U); \+(A == spot2 ), assert(on(X,spot2)),retract(top(_,spot2)), assert(top(X,spot2)), assert(move(X,A,spot2))) ;
     /* next_is_3     ->*/
     top(T, spot3), (not(preserve_alph_ord(X,T)) -> on(T,U), clear_off(U);
     (\+(A == spot3),assert(on(X,spot3)), retract(top(_,spot3)), assert(top(X,spot3)), assert(move(X,A,spot3))))
     ).


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
