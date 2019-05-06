function is_leap_year(year::Int)
    if year % 4
        if year % 100
            if year % 400
                return true
            else
                return false
            end
        end
    end
end    
