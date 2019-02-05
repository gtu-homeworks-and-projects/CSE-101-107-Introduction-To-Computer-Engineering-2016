%Prolog is a declarative programming language. This means that in prolog, you do not write out what the computer should do line by line, as in procedural languages such as C and Java.
%The general idea behind declarative languages is that you describe a situation. Based on this code, the interpreter or compiler will tell you a solution. 
%In the case of prolog, it will tell you whether a prolog sentence is true or not and, if it contains variables, what the values of the variables need to be.

%PREDICATES
male(x).
male(y).
female(a).
female(b).


parent(x,y).


%RULES
child(X,Y)	:- parent(Y,X).
sibling(X, Y) :- parent(Z, X), parent(Z, Y).

mother(X,Y) :- female(X), parent(X,Y).
father(X,Y) :- male(X), parent(X,Y).
brother(X,Y) :- male(X), sibling(X,Y).
sister(X,Y) :- female(X), sibling(X,Y).
son(X,Y) :-	parent(Y,X) ,male(X).
daughter(X,Y) :- parent(Y,X), female(X).
grandmother(X,Y) :- female(X), parent(X,Z), parent(Z,Y).
aunt(X,Y) :- child(Y,Z), sibling(Z,X).

