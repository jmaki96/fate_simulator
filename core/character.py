""" Defines Character class for modeling a character for taking damage and attacking.
"""

from enum import Enum
from typing import Dict, List, Union


class Consequence(Enum):

    Mild = 2
    Moderate = 4
    Severe = 6
    Extreme = 8


class Stress:
    """ Defines a Stress track and provides method for absorbing stress. 
    """
    _STRESS_BOX_USED: str = "used"
    _STRESS_BOX_VALUE: str = "value"

    def __init__(self, stress: int = 2) -> None:
        """ Initializes a Stress track.

        Args:
            stress (int, optional): How many Stress boxes on this Stress track. Starts at 1 and increases. Defaults to 2.
        """

        self.track: Dict[int, bool] = {}  # you cannot have multiple stress boxes of the same size.
        
        for stress_box in range(stress):
            self.track[stress_box + 1] = False

    def _get_unused_boxes(self) -> List[int]:
        """ Get all currently unused Stress boxes on the Stress track.

        Returns:
            List[int]: List of stress box sizes available
        """

        _unused_boxes: List[int] = []
        for stress_box, used in self.track.items():
            if not used:
                _unused_boxes.append(stress_box)
        
        return _unused_boxes

    @property.getter
    def remaining_stress(self) -> int:
        """ Returns how many remaining shifts could possibly be absorbed."""
        return sum(self._get_unused_boxes())

    def end_scene(self) -> None:
        """ Restore Stress as if the scene ended.
        """

        for stress_box in self.track:
            self.track[stress_box] = False

    def take_shifts(self, shifts: int, max_num_of_boxes: int = 1) -> int:
        """ Attempts to absorb shifts of damage, and records if appropriate.

        Args:
            shifts (int): How many shifts of damage to resolve
            max_num_of_boxes (int, optional): NOT YET IMPLEMENTED How many stress boxes can be used to absorb this damage. Default to 1.

        Returns:
            int: How many shifts of damage were not able to be absorbed. Could be the same as was passed.
        """

        # Bigger boxes have more utility, so always try to absorb damage in as few boxes as possible.
        



class Character:
    """ Defines a character and provides method for dealing and receiving damage and gauging how injured the character is.
    
    """

    def __init__(self, attack: int = 0, defend: int = 0, stress: int = 2, consequences: int = 3) -> None:
        """ Initialize a Character.

        Args:
            attack (int, optional): Attack skill modifier to be added to Attack rolls. Defaults to 0.
            defend (int, optional): Defend skill modifier to be added to Defend rolls. Defaults to 0.
            stress (int, optional): How many Stress boxes for absorbing damage. Start at size 1 and increases. Defaults to 2.
            consequences (int, optional): How many Consequences for absorbing damage. Starts at mild and increases. Defaults to 3.
        """

        self.attack = attack
        self.defend = defend

        for stress_box in range(stress):
            self.stress = []