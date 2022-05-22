class Tournament
  @teams = Array.new
  @wins = Array.new
  @draws = Array.new
  @losses = Array.new

    def self.tally(input)
      cloister_result = input.split("\n")
      final_element = cloister_result.size-1
      for rows in 0..final_element do
        print cloister_result[rows]
        match = cloister_result[rows].split(";")
        match = match.strip
        print match
        for a in 0..1 do
          print match[a]
          team_name = match[a].strip
          unless @teams.include? team_name
            @teams << team_name 
            @wins << 0
            @losses << 0
            @draws << 0
          end
        end
        team_a_pos = cloister_result.index match[0]
        print team_a_pos
        team_b_pos = cloister_result.index match[1]
        print team_b_pos
        # if match[2] == "win"
        #     @wins[team_a_pos] = @wins[team_a_pos] + 1
        #     @losses[team_b_pos] = @losses[team_b_pos] + 1
        # end
        # if match[2] == "loss"
        #     @losses[team_a_pos] = @losses[team_a_pos] + 1
        #     @wins[team_b_pos] = @wins[team_b_pos] + 1
        # end
        # if match[2] == "draw"
        #     @draws[team_a_pos] == @draws[team_a_pos] + 1
        #     @draws[team_b_pos] == @draws[team_b_pos] + 1
        # end

        
      end
    # print @teams
    # print @wins
    # print @draws 
    # print @losses
    return @teams

  end
end
  
# Tournament.tally("Blithering Badgers;Allegoric Alaskans;loss")
# Tournament.tally("Blithering Badgers;Allegoric Alaskans;win")
Tournament.tally("Allegoric Alaskans;Blithering Badgers;draw")
Tournament.tally("Allegoric Alaskans;Blithering Badgers;win
    Allegoric Alaskans;Blithering Badgers;win")  