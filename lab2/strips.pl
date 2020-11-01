
:- dynamic on/2.

on(a,b).    
on(b,c).    
on(c,spot1).

on_first(A) :-
    on(A,spot1).
on_first(A) :-
    on(A,X),
    on_first(X).

on_middle(A) :-
    on(A, spot2).
on_middle(A) :-
    on(A,X),
    on_middle(X).

on_last(A) :-
    on(A,spot3).
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

put_on(A,A) :-
    false.
put_on(A,B) :-
    on(A,B).
put_on(A,B) :-
    not(on(A,B)),
    \+(A == spot1),
    \+(A == spot2),
    \+(A == spot3),
    preserve_alph_ord(A,B),
    is_adjecent(A,B),
    on(A,X),
    clear_off(A),
    on(B,Y),
    clear_off(B),
    print("test"),
    retract(on(A,X)),
    assert(on(A,B)),
    assert(move(A,X,B)).


return_spot(spot1) :-
    spot1 .
return_spot(spot2) :-
    spot2 .
return_spot(spot3) :-
    spot3 .
return_spot(A) :-
    on(A,X),
    return_spot(X).

return_top(A) :-
    on(X,A)
    -> return_top(X)
    ; A .

find_next_spot(A,prev) :-
    ((on_first(A) ; on_last(A)) -> spot2 ;
     spot1
    ).
find_possible_move(A) :-
    (return_spot(A) == spot1, preserve_alph_ord(A,return_top(spot2))) -> spot2;
    (return_spot(A) == spot3, preserve_alph_ord(A,return_top(spot2))) -> spot2;
    (return_spot(A) == spot2, preserve_alph_ord(A,return_top(spot3))) -> spot3;
    (return_spot(A) == spot2, preserve_alph_ord(A,return_top(spot1))) -> spot1;
    spot1.
   
clear_off(A) :-      
    not(on(_,A)).
clear_off(A) :-
    on(X,A),
    clear_off(X),    
    retract(on(X,A)),
    ((on_first(X) ; on_last(X))
    -> ((X == a, (return_top(spot2) == c ; return_top(spot2) == b ; return_top(spot2) == spot2) )
       -> put_on(X,return_top(spot2)) ,assert(move(X,A,return_top(spot2))), assert(on(X,return_top(spot2)))
       ; (( X == b , (return_top(spot2) == c ; return_top(spot2) == spot2))
	 -> put_on(X,return_top(spot2)) ,assert(move(X,A,return_top(spot2))), assert(on(X,return_top(spot2)))
	 ; ((X == c, return_top(spot2) == spot2)
 	   -> put_on(X,return_top(spot2)) ,assert(move(X,A,return_top(spot2))), assert(on(X,return_top(spot2)))
	   ; clear_off(spot2)))
       ; ( return_top(spot3) == spot3
	 -> put_on(X,return_top(spot3)) ,assert(move(X,return_top(spot2),return_top(spot3))), assert(on(X,return_top(spot3)))
	 ; (return_top(spot1) == spot1
	   -> put_on(X,return_top(spot1)) ,assert(move(X,return_top(spot2),return_top(spot1))), assert(on(X,return_top(spot1)))
	   ; false
	   )))
    ; false).


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
