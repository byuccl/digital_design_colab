module expressions(
   input wire logic A,
   input wire logic B,
   input wire logic C,
   input wire logic D,
   output logic Q
);

logic AB, Cn, ACnD, BD, BD_n;

and(AB, A, B); 
not(Cn, C);
and(ACnD, A, Cn, D);
and(BD, B, D); 
not(BD_n, BD);
or(Q, AB, ACnD, BD_n);


endmodule
