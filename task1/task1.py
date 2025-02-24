CHIP DecoderSegment201890722 {
    IN A, B, C, D;
    OUT b;

    PARTS:
    AND (in1=A, in2=C, out=AC);
    NOT (in=AC, out=nAC);
    
    NOT (in=A, out=nA);
    AND (in1=nA, in2=D, out=nA_D);

    NOT (in=B, out=nB);
    AND (in1=nB, in2=C, out=nB_C);
    
    NOT (in=D, out=nD);
    AND (in1=B, in2=nD, out=B_nD);
    
    OR (in1=nAC, in2=nA_D, out=part1);
    OR (in1=nB_C, in2=B_nD, out=part2);
    OR (in1=part1, in2=part2, out=b);
}
