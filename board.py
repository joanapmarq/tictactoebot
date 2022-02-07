import discord
from discord import message
from discord.interactions import Interaction
from discord.ui import Button, View, view
from discord.ui.button import button
from gamelogic import GameLogic, PlayerWon


class PlayButton(discord.ui.Button):
    def __init__(self, x, y, play_callback):
        super().__init__(label=' ', style=discord.ButtonStyle.primary, row=y)
        self.x = x
        self.y = y
        self.play_callback = play_callback

    async def callback(self, interaction):
        try:
            symbol = self.play_callback(self.x, self.y)
            self.label = symbol
            await interaction.response.edit_message(view=self.view)
        except PlayerWon as e:

            for button in self.view.children:
                coordenadas_butao = (button.x, button.y)
                if coordenadas_butao == e.a or coordenadas_butao == e.b or coordenadas_butao == e.c:
                    button.style = discord.ButtonStyle.green
            self.label = e.symbol
            await interaction.response.edit_message(content=str(e), view=self.view)


class Board(discord.ui.View):
    # @discord.ui.button(label='A button', style=discord.ButtonStyle.primary)
    # async def button_callback(self, button, interaction):
    #    await interaction.response.send_message('Button was pressed', ephemeral=True)
    def __init__(self, ctx):
        self.context = ctx
        super().__init__()
        self.gamelogic = GameLogic()
        self.init_board()

    def init_board(self):
        for y in range(3):
            for x in range(3):
                self.add_item(PlayButton(x, y, self.gamelogic.play))
