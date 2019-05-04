class ResistorColorDuo
    def self.initialize
        @color_values = { 
            "black" => 0,
            "brown" => 1,
            "red" => 2,
            "orange" => 3,
            "yellow" => 4,
            "green" => 5,
            "blue" => 6,
            "violet" => 7,
            "grey" => 8,
            "white" => 9}
    end

    def self.value([color_1, color_2])
        p color_1: color_1, color_2: color_2
        (@color_values[color_1].to_s + @color_values[color_2].to_s).to_i
    end
end

ResistorColorDuo.value(["black", "blue"])