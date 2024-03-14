module full_add(
  input logic a, b, cin,
  output logic s, co
  );
  //Answer provided
  assign s = a^b^cin;
  assign co = (a&b)|(a&cin)|(b&cin);
  endmodule
