class ExcelConfig:
    TABLE_FIRST_ROW_IDX = 21
    SIGNS_ROW_IDX_1 = 24
    SIGNS_ROW_IDX_2 = 26
    SIGNS_ROW_IDX_BTW = 25
    PRACT_HEADERS_ROW_IDX = 31
    LAST_ROW_IDX = 36
    FIRST_FORMULAS_COLUMN = 55
    LAST_FORMULAS_COLUMN = 62

    theoretical_edu_formula = '=COUNTIF(C{rowIdx}:BB{rowIdx},"")+COUNTIF(C{rowIdx}:BB{rowIdx},"М")'
    examen_session_formula = '=COUNTIF(C{rowIdx}:BB{rowIdx},"С")'
    practice_formula = '=COUNTIF(C{rowIdx}:BB{rowIdx},"П")'
    qualification_work_formula = '=COUNTIF(C{rowIdx}:BB{rowIdx},"КР")'
    attestation_formula = '=COUNTIF(C{rowIdx}:BB{rowIdx},"А")'
    holidays_formula = '=COUNTIF(C{rowIdx}:BB{rowIdx},"К")'
    summary_row_formula = '=SUM(BC{rowIdx}:BH{rowIdx})'

    summary_theoretical_edu_formula = '=SUM(BC{firsRow}:BC{lastRow})'
    summary_examen_session_formula = '=SUM(BD{firsRow}:BD{lastRow})'
    summary_practice_formula = '=SUM(BE{firsRow}:BE{lastRow})'
    summary_qualification_work_formula = '=SUM(BF{firsRow}:BF{lastRow})'
    summary_attestation_formula = '=SUM(BG{firsRow}:BG{lastRow})'
    summary_holidays_formula = '=SUM(BH{firsRow}:BH{lastRow})'
    summary_total_formula = '=SUM(BI{firsRow}:BI{lastRow})'

    ROW_FORMULAS = [
        theoretical_edu_formula,
        examen_session_formula,
        practice_formula,
        qualification_work_formula,
        attestation_formula,
        holidays_formula,
        summary_row_formula
    ]

    SUMMARY_FORMULAS = [
        summary_theoretical_edu_formula,
        summary_examen_session_formula,
        summary_practice_formula,
        summary_qualification_work_formula,
        summary_attestation_formula,
        summary_holidays_formula,
        summary_total_formula
    ]

    COURSE_IDXS = ['I', 'II', 'III', 'IV', 'V']