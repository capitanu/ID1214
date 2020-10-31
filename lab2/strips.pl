/* prolog tutorial 2.19  Actions and plans */

:- dynamic on/2.

on(a,b).    
on(b,c).    
on(c,spot1).

on_first(A) :-
    on(A,spot1).
on_first(A) :-
    on(A,X),
    on_first(X).

on_last(A) :-
    on(A,spot3).
on_last(A) :-
    on(A,X),
    on_last(X).

put_on(A,B) :-
    on(A,B).
put_on(A,B) :-
    not(on(A,B)),
    \+(A == spot1),
    \+(A == spot2),
    \+(A == spot3),
    (\+(A == c),\+(B == b)),
    (\+(A == c),\+(B == a)),
    ((A == b),\+(B == a)),
    (on_first(A),on_last(B)),
    (on_first(B),on_last(A)),
    \+(A == B),
    clear_off(A),    
    clear_off(B),
    on(A,X),
    retract(on(A,X)),
    assert(on(A,B)),
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
    retract(on(X,A)),
    (put_on(X,spot2), assert(move(X,A,spot2)), assert(on(X,spot2));
     put_on(X,spot3), assert(X,spot3),assert(move(X,A,spot3))).


do(Glist) :- 
    valid(Glist), 
    do_all(Glist,Glist). 

valid(_).            

do_all([G|R],Allgoals) :-          /* already true now */
    call(G),
    do_all(R,Allgoals),!.         /* continue with rest of goals */

do_all([G|_],Allgoals) :-          /* must do work to achieve */
    achieve(G),
    do_all(Allgoals,Allgoals).    /* go back and check previous goals */
do_all([],_Allgoals).              /* finished */

achieve(on(A,B)) :-
    put_on(A,B).
