select * from (
  select listagg(c1,',') within group (order by C1) as d1,d2,d3,d4,d5,d6,d7,d8,d9,d10,d11,d12,d13,d14 from (
    select c1,listagg(c2,',') within group (order by C2) as d2,d3,d4,d5,d6,d7,d8,d9,d10,d11,d12,d13,d14 from (
      select c1,c2,listagg(c3,',') within group (order by C3) as d3,d4,d5,d6,d7,d8,d9,d10,d11,d12,d13,d14 from (
        select c1,c2,c3,listagg(c4,',') within group (order by C4) as d4,d5,d6,d7,d8,d9,d10,d11,d12,d13,d14 from (
          select c1,c2,c3,c4,listagg(c5,',') within group (order by C5) as d5,d6,d7,d8,d9,d10,d11,d12,d13,d14 from (
            select c1,c2,c3,c4,c5,listagg(c6,',') within group (order by C6) as d6,d7,d8,d9,d10,d11,d12,d13,d14 from (
              select c1,c2,c3,c4,c5,c6,listagg(c7,',') within group (order by C7) as d7,d8,d9,d10,d11,d12,d13,d14 from (
                select c1,c2,c3,c4,c5,c6,c7,listagg(c8,',') within group (order by C8) as d8,d9,d10,d11,d12,d13,d14 from (
                  select c1,c2,c3,c4,c5,c6,c7,c8,listagg(c9,',') within group (order by C9) as d9,d10,d11,d12,d13,d14 from (
                    select c1,c2,c3,c4,c5,c6,c7,c8,c9,listagg(c10,',') within group (order by C10) as d10,d11,d12,d13,d14 from (
                      select c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,listagg(c11,',') within group (order by C11) as d11,d12,d13,d14 from (
                        select c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11,listagg(c12,',') within group (order by C12) as d12,d13,d14 from (
                          select c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11,c12,listagg(c13,',') within group (order by C13) as d13,d14 from (
                            select c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11,c12,c13,listagg(c14,',') within group (order by C14) as d14 from test_ly_01 t 
                            group by c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11,c12,c13
                          )lv1 group by c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11,c12,d14
                        )lv2 group by c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11,d13,d14
                      )lv3 group by c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,d12,d13,d14
                    )lv4 group by c1,c2,c3,c4,c5,c6,c7,c8,c9,d11,d12,d13,d14
                  )lv5 group by c1,c2,c3,c4,c5,c6,c7,c8,d10,d11,d12,d13,d14
                )lv6 group by c1,c2,c3,c4,c5,c6,c7,d9,d10,d11,d12,d13,d14
              )lv7 group by c1,c2,c3,c4,c5,c6,d8,d9,d10,d11,d12,d13,d14
            )lv8 group by c1,c2,c3,c4,c5,d7,d8,d9,d10,d11,d12,d13,d14
          )lv9 group by c1,c2,c3,c4,d6,d7,d8,d9,d10,d11,d12,d13,d14
        )lv10 group by c1,c2,c3,d5,d6,d7,d8,d9,d10,d11,d12,d13,d14
      )lv11 group by c1,c2,d4,d5,d6,d7,d8,d9,d10,d11,d12,d13,d14
    )lv12 group by c1,d3,d4,d5,d6,d7,d8,d9,d10,d11,d12,d13,d14
  )lv13 group by d2,d3,d4,d5,d6,d7,d8,d9,d10,d11,d12,d13,d14
) order by 1,2,3,4,5,6,7,8,9,10,11,12,13
