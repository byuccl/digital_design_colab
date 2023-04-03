module add_8(
  input logic cin,
  input logic [7:0] a, b,
  output logic [7:0] s,
  output logic co
  );
  //Answer Provided
  logic co0,co1,co2,co3,co4,co5,co6;
  full_add zero(.a(a[0]), .b(b[0]), .cin(cin), .co(co0), .s(s[0]));
  full_add one(.a(a[1]), .b(b[1]), .cin(co0), .co(co1), .s(s[1]));
  full_add two(.a(a[2]), .b(b[2]), .cin(co1), .co(co2), .s(s[2]));
  full_add three(.a(a[3]), .b(b[3]), .cin(co2), .co(co3), .s(s[3]));
  full_add four(.a(a[4]), .b(b[4]), .cin(co3), .co(co4), .s(s[4]));
  full_add five(.a(a[5]), .b(b[5]), .cin(co4), .co(co5), .s(s[5]));
  full_add six(.a(a[6]), .b(b[6]), .cin(co5), .co(co6), .s(s[6]));
  full_add seven(.a(a[7]), .b(b[7]), .cin(co6), .co(co), .s(s[7]));

 endmodule
