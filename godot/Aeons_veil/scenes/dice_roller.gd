extends Panel


# Dice Buttons
@onready var D4button = $VBoxContainer/DiceButtonContainer/MarginContainer/D4Button
@onready var D6button = $VBoxContainer/DiceButtonContainer/MarginContainer2/D6Button
@onready var D8button = $VBoxContainer/DiceButtonContainer/MarginContainer3/D8Button
@onready var D10button = $VBoxContainer/DiceButtonContainer/MarginContainer4/D10Button
@onready var D12button = $VBoxContainer/DiceButtonContainer/MarginContainer5/D12Button
@onready var D100button = $VBoxContainer/DiceButtonContainer/MarginContainer6/D100Button
@onready var D20button = $VBoxContainer/DiceButtonContainer/MarginContainer7/D20Button

# Dice Pool Label	
@onready var dice_pool_label= $VBoxContainer/dicePoolLabel

# Modifier Buttons
@onready var plus_one_button = $VBoxContainer/ModifierButtonContainer/MarginContainer/AddOneModifier
@onready var minus_one_button = $VBoxContainer/ModifierButtonContainer/MarginContainer2/misusOneModifier

# Modifier Label
@onready var modifier_label = $VBoxContainer/modifierLabel

#Results Labels
@onready var rollButton = $VBoxContainer/RollButtonMargin/rollButton
@onready var roll_pool_label = $VBoxContainer/MarginContainer/DiceRolledLabel
@onready var total_label = $VBoxContainer/TotalLabel

var dice_pool = []
var modifier = 0
var result_pool = []
var total = 0


func _ready():
	D4button.pressed.connect (func(): add_die_to_pool("D4"))
	D6button.pressed.connect(func(): add_die_to_pool("D6"))
	D8button.pressed.connect(func(): add_die_to_pool("D8"))
	D10button.pressed.connect(func():add_die_to_pool("D10"))
	D12button.pressed.connect(func():add_die_to_pool("D12"))
	D100button.pressed.connect(func():add_die_to_pool("D100"))
	D20button.pressed.connect(func():add_die_to_pool("D20"))
	plus_one_button.pressed.connect(func():determine_modifier(1))
	minus_one_button.pressed.connect(func():determine_modifier(-1))
	
	rollButton.pressed.connect(func():roll(dice_pool,modifier))
	
func add_die_to_pool(die_type: String) -> void:
	dice_pool.append(die_type)
	dice_pool_label.text = "Dice to Roll: " + ", ".join(dice_pool)

func determine_modifier(change) -> void:
	modifier = modifier + change
	modifier_label.text = "Modifier: " + str(modifier)
	
func roll(dice_pool,modifier) ->void:
	result_pool.clear()
	var numeric_results = []
	
	for die in dice_pool:
		var sides = int(die.substr(1))  # removes "D" and converts to int
		var roll_result = randi_range(1, sides)
		numeric_results.append(roll_result)
		result_pool.append(str(roll_result))  # for display purposes

	var total = 0
	for num in numeric_results:
		total += num
		
	total += modifier

	# Update the UI
	roll_pool_label.text = "Roll Result: " + ", ".join(result_pool)
	total_label.text = "Total: " + str(total)

	# Reset after roll
	dice_pool.clear()
	modifier = 0
	dice_pool_label.text = "Dice Pool: "
	modifier_label.text = "Modifier: 0"

	
