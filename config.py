from .ankiaddonconfig import ConfigManager, ConfigWindow

conf = ConfigManager()


def setup_config():
    conf.use_custom_window()
    conf.on_window_open(_on_config_window_open)
    conf.add_config_tab(_general_tab)


def _on_config_window_open(conf_window: ConfigWindow) -> None:
    """Ankiaddonconfig is used here in a non-standard way for configuring the note type options.
    The options don't really need to be saved in the config and they are overwritten with the values on the model when
    the config window is opened.
    """
    from .model import (
        config_values_from_model,
        add_or_update_model,
        update_model_options_with_config_values,
    )

    # Create the model if it doesn't exist
    add_or_update_model()

    # Load the config values from the model
    d = config_values_from_model()
    for key in d:
        conf.set(key, d[key])

    # Update the model when the config is saved
    conf_window.execute_on_save(update_model_options_with_config_values)


def _general_tab(conf_window: ConfigWindow) -> None:
    tab = conf_window.add_tab("General")
    
    
    tab.space(5)    
    tab.text("Border Actions", bold=True)
    tab.hseparator()
    tab.checkbox("swapLeftAndRightBorderActions", "Swap left and right border actions")
    
    
    tab.space(5)    
    tab.text("Cloze Style", bold=True)
    tab.hseparator()
    tab.checkbox("underlineRevealedPseudoClozes", "Underline revealed pseudo clozes")
    tab.checkbox("underlineRevealedGenuineClozes", "Underline revealed genuine clozes")
    
    tab.space(5)    
    tab.text("Cloze Behavior", bold=True)
    tab.hseparator()
    tab.checkbox("showHintsForPseudoClozes", "Show hints for pseudo clozes")
    tab.checkbox("revealPseudoClozesByDefault", "Reveal pseudo clozes by default")

    tab.space(5)
    tab.text("Auto Scroll to relevant cloze", bold=True)
    tab.hseparator()
    tab.checkbox("scrollToClozeOnToggle", "Scroll to cloze on toggle")
    tab.checkbox("animateScroll", "Animate scrolling")

    tab.stretch()
    
    tabS = conf_window.add_tab("Shortcut")
    tabS.space(5)    
    tabS.text("Shorcuts", bold=True)
    tabS.hseparator()
    tabS.shortcut_input(
        "revealNextGenuineClozeShortcut", "Shortcut to reveal next genuine cloze"
    )
    tabS.shortcut_input(
        "revealAllGenuineClozesShortcut", "Shortcut to reveal all genuine clozes"
    )
    tabS.shortcut_input(
        "revealNextPseudoClozeShortcut", "Shortcut to reveal next pseudo cloze"
    )
    tabS.shortcut_input(
        "revealAllPseudoClozesShortcut", "Shortcut to reveal all pseudo clozes"
    )
    tabS.stretch()
    
    
    tabMod = conf_window.add_tab("+ mod")
    
    tabMod.space(5)
    tabMod.text_input(
        "googleTranslateIntoLanguage", "Two characters of your native language code (en and similar)"
    )
    tabMod.checkbox("ttsSoundEnable", "Enable voice-over using TTS")
    tabMod.checkbox("inputEnable", "Allow text input field")
    tabMod.checkbox("floatingPanelEnable", "Allow floating panel when selecting text")
    
    tabMod.stretch()
    
    
    tabA = conf_window.add_tab("About")
    txtAuthors = """
    <p>
    Author of the addon modification: <a href="https://github.com/AndreyKaiu" rel="noopener noreferrer">https://github.com/AndreyKaiu</a><br>
    Addon version: 1.14, date: 2026-07-15<br>
    <br>
    See my other addons and decks here: <a href="https://ankiweb.net/shared/by-author/1188253433" rel="noopener noreferrer">https://ankiweb.net/shared/by-author/1188253433</a><br>
    <br>
    This addon is a modification of the addon <a href="https://ankiweb.net/shared/info/1990296174" rel="noopener noreferrer">"Enhanced Cloze (for Anki 2.1)"</a>. Read all the information from there!<br>
    <br>
    I would like to express my gratitude to all the authors who create add-ons and the Anki program!
    <hr>
   This add-on automatically installs the new "Cloze TTS-Input" note type.<br>
As the name suggests, it offers both TTS voiceover and the ability to enter text for verification directly in the field. Voiceover can be useful when learning languages, and text input allows you to check the spelling of a term (or word, if it's a foreign language).<br>
Added features can be configured in the "+ mod" tab.<br>
Please note that hotkeys cannot be just a letter, as this will interfere with text input!<br>
Additional configuration is available in the map design, but it's customizable by people with at least some understanding of JavaScript and HTML. If you create a copy of this note type, everything will work without this add-on, but the add-on itself can only manage the "Cloze TTS-Input" note type.
    </p>
    """
    tabA.text(txtAuthors, bold=False, html=True, multiline=True)
    
  
    
    tabA.stretch()
    
    
