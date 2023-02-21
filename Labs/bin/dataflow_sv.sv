module dataflow_sv(
    input logic[15:0] sw,
    input wire logic btnu, btnd, btnl, btnr,
    output logic[15:0] led
);

always_comb begin
    led = sw;
    if(btnl) begin
        led[15:8] = 8'h00;
        led[7:0] = sw[15:8]^sw[7:0];
    end
    else if(btnr) begin
        led[15:1] = 15'd0;
        led[0] = (sw[0]&~sw[1])|(sw[2]);
    end
    else if(btnd) begin
        led = sw << 3;
    end
    else if(btnu) begin
        if(sw[1] && !sw[0]) begin
            if((sw[6:3] > 12) || (sw[6:3] == 0))
                led = 16'h0000;
            else 
                led = 16'hFFFF;
        end
        else if(sw[0] && !sw[1]) begin
            if((sw[6:3] >= 7) && (sw[6:3] <= 11) && (sw[2] == 0))
                led = 16'hFFFF;
            else if((sw[6:3] >= 1) && (sw[6:3] <= 10) && (sw[2] == 1))
                led = 16'hFFFF;
            else if((sw[6:3] == 12) && (sw[2] == 1))
                led = 16'hFFFF;
            else 
                led = 16'h0000;
        end
        else
            led = 16'h0000;
    end
end

endmodule
