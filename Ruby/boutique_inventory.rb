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

    def cheap
      array_cheap = Array.new
      for item in @items do
        if item[:price] < 30 then
          array_cheap.append(item)
        end
      end
      array_cheap
    end

    def out_of_stock
      array_empty = Array.new
      for item in @items do
        if item[:quantity_by_size] == {} then
          array_empty.append(item)
        end
      end
      return array_empty
    end
  
  end
  