function deleteNote(noteID) {
    fetch('/delete-note',{
        method: 'POST',
        bode: JSON.stringify({ noteId: noteID})
    }).then((_res) => {
        window.location.href = "/notes"
    });
}