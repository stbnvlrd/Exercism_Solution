class BoutiqueInventory
    def initialize(items)
      @items = items
    end
  
    def item_names
      array_names = Array.new
      for item in @items do
        array_names.append(item[:name])
      end
      array_names_sorted = array_names.sort
    end
  end
  