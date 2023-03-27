module function4(
   input logic btnu, student, prof, pm,
   input logic[3:0] hour,
   input logic[8:0] sw,
   output logic[15:0] led
);
//Answer provided
always_comb begin
   if(btnu) begin
      if(prof && !student) begin
            if((hour > 12) || (hour == 0))
                led = 16'h0000;
            else 
                led = 16'hFFFF;
        end
        else if(student && !prof) begin
            if((hour >= 7) && (hour <= 11) && (pm == 0))
                led = 16'hFFFF;
            else if((hour >= 1) && (hour <= 10) && (pm == 1))
                led = 16'hFFFF;
            else if((hour == 12) && (hour == 1))
                led = 16'hFFFF;
            else 
                led = 16'h0000;
        end
        else
            led = 16'h0000;
   end
   else begin
       led[15:7] = sw;
       led[6:3] = hour;
       led[2:0] = {pm, prof, student};
   end
end

endmodule
