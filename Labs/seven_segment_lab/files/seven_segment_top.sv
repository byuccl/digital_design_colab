module seven_segment_top (
  input logic [3:0] sw,
  input logic btnc,
  output logic [7:0] segment,
  output logic [3:0] anode
);

  //Top module for seven_segment
  assign anode = 0;
  seven_segment ss(.data(sw), .segment(segment[6:0]));
  assign segment[7] = btnc;
endmodule
