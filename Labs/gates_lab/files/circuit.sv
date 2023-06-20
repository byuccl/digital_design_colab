module circuit(
   input wire logic A,
   input wire logic B,
   input wire logic C,
   input wire logic D,
   output logic Q
);

logic e, f, g, h, k, q;

and(e, A, B); 
or(f, B, C); 
and(g,C,D); 
not(h,g);
and(k,f,h);
or(q,k,e);
not(Q,q); 


endmodule

